db.createUser({
  user: "TestUser",
  pwd: "TestPassword",
  roles: [
    {
      role: "readWrite",
      db: "shortlinks"
    }
  ]
})