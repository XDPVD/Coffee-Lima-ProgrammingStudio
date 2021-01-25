const Sequelize = require('sequelize');


const sequelize = new Sequelize('uptasknodedb', 'root', 'admin', {
  host: 'localhost',
  dialect: 'mysql',
  port: '3306',
  define:{
      timestamps:false, //Nos evita tener errores inesperados
  }
});

module.exports = sequelize