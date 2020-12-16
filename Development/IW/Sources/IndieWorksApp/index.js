const express = require('express') //Importamos Express

const router = require('./routes') //Importa las rutas

const path = require('path'); //Importa la librería path , sirve para utilizar las direcciones del sistema

const bodyParser = require('body-parser') //Importando bodyparser

const db = require('./config/db'); //Importando el ORM

const helpers = require('./helpers'); //Importando helpers

//Archivos internos ./    externos -> "nada"


require('./models/db_proyectos.js') //Importamos el script del modelo
db.sync() //Sincronizamos con la base de datos.
    .then(() => console.log('Conectando al servidor'))
    .catch(error => console.log(error))

const app = express(); //Crea la app express

app.use(express.static('public')) //Carga los archivos estáticos




app.set('view engine','pug');
app.set('views',path.join(__dirname,'./views'));


app.use((req,res,next)=>{
    res.locals.vardump = helpers.vardump; //res.locals crea variables para que sean accesibles desde
    //cualquier parte de los scripts o vistas
    next();
})



app.use(bodyParser.urlencoded({extend: true}))


app.use('/',router());


app.listen(3000); //Establece el puerto en el que se crea el servidor

