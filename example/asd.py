from pysondb import db


a = db.getDb("test.json")
#a.add({
   # "task": "task1",
  #  "desc": "a task",
   # "status": "active",
   # "settings": {"user": "me", "language": "en"}
  #  })

a.updateById(241814208588241594, {
    "settings": {"user": "another", "language": "ezxcn"}
    })