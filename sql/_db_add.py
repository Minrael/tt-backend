import postgresql 


with postgresql.open('pq://postgres:postgres@localhost:5432/back') as db: 
    ins = db.prepare(
        "INSERT INTO users (login, password) VALUES ($1, $2)"
    ) 	
    ins("afiskon", "123")
