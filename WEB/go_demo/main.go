package main

import (
	"database/sql"
	"encoding/json"
	"log"
	"net/http"
	"reflect"

	_ "github.com/mattn/go-sqlite3"
)

type JChar struct {
	Id                       int
	Pron, Hiragana, Katagana string
}

func main() {
	http.HandleFunc("/api/chars", collectionHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func collectionHandler(w http.ResponseWriter, r *http.Request) {
	method := r.Method
	if method == "GET" {
		data, err := getAll()
		if err != nil {
			http.Error(w, "Server Error", 500)
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	} else if method == "POST" {
		var data JChar
		r.ParseForm()
		for k, v := range r.Form {
			reflect.ValueOf(&data).Elem().FieldByName(k).SetString(v[0])
		}
		err := addNew(&data)
		if err != nil {
			http.Error(w, "Server Error", 500)
		} else {
			w.Header().Set("Content-Type", "application/json")
			res := struct {
				Status  int
				Message string
			}{1, "ok"}
			json.NewEncoder(w).Encode(res)
		}
	} else {
		http.Error(w, "method not supprted", 405)
	}
}

var db, _ = sql.Open("sqlite3", "./fifty_sound.db")

func getAll() ([]JChar, error) {
	rows, err := db.Query("SELECT * FROM FIFTY_SOUND;")
	checkErr(err)
	defer rows.Close()
	var data []JChar
	var id int
	var pron, hiragana, katagana string
	for rows.Next() {
		rows.Scan(&id, &pron, &hiragana, &katagana)
		data = append(data, JChar{id, pron, hiragana, katagana})
	}
	err = rows.Err()
	return data, err
}

func addNew(jc *JChar) error {
	tx, err := db.Begin()
	checkErr(err)
	stmt, err := tx.Prepare("INSERT INTO FIFTY_SOUND (pron, hiragana, katagana) VALUES (?, ?, ?)")
	checkErr(err)
	defer stmt.Close()
	_, err = stmt.Exec(jc.Pron, jc.Hiragana, jc.Katagana)
	tx.Commit()
	return err
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
