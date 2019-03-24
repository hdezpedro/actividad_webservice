import web

db_host = 'd5x4ae6ze2og6sjo.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'euwd9h6p5k605t8z'
db_user = 'cc6hx3z3huxqsogi'
db_pw = 'u99oplxd3ojzupx0'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )