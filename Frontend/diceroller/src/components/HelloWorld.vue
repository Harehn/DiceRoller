<template>
  <div class="hello">
    <!-- Waiting for backend message and loader -->
    <div v-if="!backend_awake">
      <p style="display: inline-block;padding-right:5px;">Waking up backend... Some functionalities may not work right away... Please wait...</p> 
      <div class="loader"></div>
    </div>

    <!--Welcome Message-->
    <h1>{{ msg }}</h1>  

    <!--Element for Dice roll input-->
    <div>
      <label for='dice_input'>Dice: </label>
      <input type='text' id='dice_input' name='dice_input' placeholder="eg. 8d6"  @keyup.enter="writeText">
      <p id=space>X</p>
      <input type='button' value='Roll' @click='writeText'>
      <p id=space>X</p>
      <help help_msg="8d6 indicates 8 6-sided dice are rolled and the total of the rolls are displayed."/>
    </div>

    <!--Clear history button-->
    <div>
      <input type='button' value='Clear History' @click='clear'>
    </div>

    <!--Clear history button-->
    <!-- <div>
      <input type='button' value='Download History' @click='dwld'>
    </div> -->

    <!--History-->
    <div id="roll" v-if='results.length != 0'>
      <p class="iroll" v-for="result in results"><b>{{result[0]}}:</b> {{result[1]}}</p>
    </div>

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
    in_dev:false,
    backend_awake:false
   }
  },
  methods: {
    async writeText() {
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
    },
    async dwld(){
      const url = "http://localhost:5000/doc";
      await fetch(url)
      .then((res)=>res.blob())
      
    }
  },
  mounted() {
    //https://stackoverflow.com/a/58475472/28974846
    if (process.env.NODE_ENV == 'development'){
       this.in_dev = true;
       console.log("App was opened in DEVELOPMENT");
       var api_path = 'http://localhost:5000/roll?roll=';
       console.log("Calling Backend...")
        fetch(api_path)
        .then(res => res.json())
        .then(data => data['message'])
        .then(data => console.log(data))
        .then(data => this.backend_awake=true)
        .catch(err => console.log(err));
    }else{
       console.log("App was opened in PRODUCTION");
       var api_path = 'https://diceroller-uwe7.onrender.com/wake';
       console.log("Calling Backend...")
        fetch(api_path)
        .then(res => res.json())
        .then(data => data['message'])
        .then(data => console.log(data))
        .then(data => this.backend_awake=true)
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
#space {
  display: inline-block;
  visibility: hidden;
  font-size: 6px;
}

#roll {
  border-color: black;
  border-radius: 10px;
  border-width: 1px;
  border-style: solid;
  background-color: lightcyan;
  max-width: 400px;
  margin-right: auto;
  margin-left: auto;
  overflow-y: scroll;
  max-height: 500px;
  min-height: auto;
}

.iroll {
  border-color: black;
  border-radius: 10px;
  border-width: 1px;
  border-style: solid;
  background-color: lightblue;
  max-width: 390px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 4px;
  margin-bottom: 4px;
  padding: 0px;
}

.loader {
  --s: 10px;
  
  --_d: calc(0.353*var(--s));
  width: calc(var(--s) + var(--_d));
  aspect-ratio: 1;
  clip-path: polygon(var(--_d) 0,100% 0,100% calc(100% - var(--_d)),calc(100% - var(--_d)) 100%,0 100%,0 var(--_d));
  background:
    conic-gradient(from -90deg at var(--s) var(--_d),
     #fff 135deg,#666 0 270deg,#aaa 0);
  animation: l1 1s infinite cubic-bezier(0.5,300,0.5,-300);
  display: inline-block;
}
@keyframes l1{
  50%,100% {transform:translateY(0.1px)}
}

</style>