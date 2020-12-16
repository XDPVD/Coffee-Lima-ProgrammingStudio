const Sequelize = require('sequelize');

const db = require('../config/db') //Importamos la base de datos

const Proyectos = db.define('proyectos',{
    id :{
        type: Sequelize.INTEGER,
        primaryKey: true, //reserverd word
        autoIncrement: true //reserverd word
    },
    nombre : Sequelize.STRING,
    url : Sequelize.STRING
})

module.exports = Proyectos;