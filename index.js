const express =  require('express')
const app = express()
const path = require('path')
const bodyParser = require('body-parser');
const {default:weaviate} = require("weaviate-ts-client");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'views')));
let initial_path = path.join(__dirname, "views");

const client = weaviate.client({
  scheme: 'http',
  host: 'localhost:8000',
});

//rendering home page
app.get('/', (req, res) => {
    res.render(path.join(initial_path, "search.ejs"),{answer:[], error: null, question: null});
})

//perform query for seached text
app.post('/search', async (req, res) => {
    let question = req.body['searched_data'];
    let type = req.body['type'];
    let answer = null;
    console.log(question, type);
    if (type === 'DentalCondition') {
      answer = await runConditionQuery(question);
    } else if ('DentalProcedure') {
      answer = await runProcedureQuery(question);
    } else if ('DentalEquipment') {
      answer = await runEquipmentQuery(question);
    } else if ('DentalMaterial') {
      answer = await runMaterialQuery(question);
    } else if ('Dentist') {
      answer = await runDentistQuery(question);
    }
    console.log(answer, 'return')
    if (answer) {
      res.render(path.join(initial_path, "search.ejs"),{answer:answer, type: type, error: null, question:question});
    } else {
      res.render(path.join(initial_path, "search.ejs"),{answer:[], type: type, error: 'server connection error!',question:question})
    }
})

async function runConditionQuery(question) {
  return new Promise((resolve, reject) => {
    client.graphql
      .get()
      .withClassName('DentalCondition')
      .withFields([ 'name', 'description', 'symptoms', 'treatments'])
      .withNearText({
          concepts: [question],
          distance: 0.7
      })
      .withLimit(1)
      .do()
      .then(info => {
        console.log(info['data']['Get']['DentalCondition'])
        resolve(info['data']['Get']['DentalCondition'])
      })
      .catch(err => {
          console.error(err.response)
          resolve(null)
      })  
  }) 
}
function runEquipmentQuery(question) {
  return new Promise((resolve, reject) => {
    client.graphql
      .get()
      .withClassName('DentalEquipment')
      .withFields([ 'name', 'description', 'procedure', 'cost'])
      .withNearText({
          concepts: [question],
          distance: 0.7
      })
      .withLimit(1)
      .do()
      .then(info => {
        resolve(info['data']['Get']['DentalEquipment'])
      })
      .catch(err => {
          console.error(err.response)
          resolve(null)
      })  
    }) 
}
function runMaterialQuery(question) {
  return new Promise((resolve, reject) => {
    client.graphql
      .get()
      .withClassName('DentalMaterial')
      .withFields([ 'name', 'description', 'procedure', 'cost'])
      .withNearText({
          concepts: [question],
          distance: 0.7
      })
      .withLimit(1)
      .do()
      .then(info => {
        resolve(info['data']['Get']['DentalMaterial'])
      })
      .catch(err => {
          console.error(err.response)
          resolve(null)
      })  
    }) 
  }
function runProcedureQuery(question) {
  return new Promise((resolve, reject) => {
    client.graphql
      .get()
      .withClassName('DentalProcedure')
      .withFields([ 
        'name', 
        'description', 
        'materials{... on DentalMaterial{name description}}',
        'equipment{... on DentalEquipment{name description}}',
        'condition{... on DentalCondition{name description}}',
      ])
      .withNearText({
          concepts: [question],
          distance: 0.7
      })
      .withLimit(1)
      .do()
      .then(info => {
        resolve(info['data']['Get']['DentalProcedure'])
      })
      .catch(err => {
          console.error(err)
          resolve(null)
      })  
    }) 
  }

app.listen(process.env.PORT || 4000)