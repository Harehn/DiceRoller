<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  <div>
  <label for='dice_input'>Dice: </label>
  <input type='text' id='dice_input' name='dice_input'  @keyup.enter="writeText">
  <input type='button' value='Roll' @click='writeText'>
  </div>

  <div>
    <input type='button' value='Clear History' @click='clear'>
  </div>

  <div v-if='rolled'>
  <p v-for="result in results"><b>{{result[0]}}:</b> {{result[1]}}</p>
  </div>

  <help/>
  </div>
</template>

<script>

import Help from './Help.vue'

export default {
  name: 'HelloWorld',
  components: {
    Help
  },
  props: {
    msg: String
  },
  data (){
   return {
    members: [],
    results: [],
    rolled: false,
    in_dev:false
   }
  },
  methods: {
    async writeText() {
      this.rolled = true;
      var dice_val = document.getElementById("dice_input").value;
      dice_val = dice_val.replaceAll(" ", "")
      var found = dice_val.match(/^[0-9d+-]*/)
      found = found[0]
      if(found.length != dice_val.length){
        console.log("Error in string formatting")
        this.results.unshift([dice_val, "Incorrect dice string"])
        return
      }
      var dice = dice_val.replace("+","%2b")
      //https://diceroller-uwe7.onrender.com/roll?roll=33
      var api_path = 'https://diceroller-uwe7.onrender.com/roll?roll='
      if (this.in_dev){api_path =  'http://localhost:5000/roll?roll='}
      api_path = api_path.concat(dice)
      console.log(api_path)
      var currResult = await fetch(api_path)
      .then(res => res.json())
      .then(response => response['result'])
      .catch(err => console.log(err));
      this.results.unshift([dice_val, currResult])
    },
    clear(){
      this.results = []
    }
  },
  mounted() {
    //https://stackoverflow.com/a/58475472/28974846
    if (process.env.NODE_ENV == 'development'){
       this.in_dev = true;
       console.log("App was opened in DEVELOPMENT");
    }else{
       console.log("App was opened in PRODUCTION");
       var api_path = 'https://diceroller-uwe7.onrender.com/wake';
       console.log("Calling Backend...")
        fetch(api_path)
        .then(res => res.json())
        .then(data => data['message'])
        .then(data => console.log(data))
        .catch(err => console.log(err));
    }
    //console.log(process.env.NODE_ENV == 'development'); // OUTPUT: development
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
