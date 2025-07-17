from sanic import Sanic

app = Sanic("mlv")
app.static('/static/', './static/')
app.static("/", "index.html", name="index")
app.static("/home", "home.html", name="home")
app.static("/item", "item.html", name="item")
