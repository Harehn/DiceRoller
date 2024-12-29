<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  <div>
  <label for='dice_input'>Dice: </label>
  <input type='text' id='dice_input' name='dice_input'>
  <input type='button' value='Roll' @click='writeText'>
  </div>

  <div v-if='rolled'>
  <p v-for="result in results">{{result}}</p>
  </div>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data (){
   return {
    members: [],
    results: [],
    rolled: false
   }
  },
  methods: {
    async writeText() {
      this.rolled = true;
      var diceType = document.getElementById("dice_input").value;
      //https://diceroller-uwe7.onrender.com/roll?roll=33
      var currResult = await fetch(`https://diceroller-uwe7.onrender.com/roll?roll=${diceType}`)
      .then(res => res.json())
      .then(response => response['result'])
      .catch(err => console.log(err));
      this.results.unshift(currResult)
    }
  },
  mounted() {
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
