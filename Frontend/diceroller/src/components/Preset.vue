<template>
    <h1>Preset</h1>
    <table>
      <tr v-for="preset in dice_presets">
        <th>{{ preset["PresetName"] }}</th>
        <th>
          <p v-for="roll in preset['Rolls']">{{ roll[0]}} {{ roll[1] }}</p>
        </th>
        <th>
          <input type='button' value='Roll' @click='roll_preset(preset)'>
        </th>
        <th>

        </th>
      </tr>
    </table>

    <div>
      <input type='button' value='Clear History' @click='clear'>
  </div>

    <div id="roll" v-if='results.length != 0'>
      <div class="iroll" v-for="result in results">
        <p class="header"><u>{{result[0]}}</u></p>
        <p class="compact" v-for="roll in result[1]">
          <b>{{roll[0]}}({{ roll[1] }}):</b> {{roll[2]}} 
        </p>
      </div>
    </div>
    
</template>
  
<script>
  export default {
    name: 'Preset',
    data (){
     return {
      dice_presets:[],
      results:[]
     }
    },
    methods: {
      async roll_preset(preset) {
        var rolls = preset["Rolls"];
        var monster = preset["PresetName"]
        var roll_results = []
        for (const roll of rolls){
          var name = roll[0]
          var dice_val = roll[1]
          dice_val = dice_val.replaceAll(" ", "")
          var dice = dice_val.replace("+","%2b")
          //https://diceroller-uwe7.onrender.com/roll?roll=3d6
          var api_path = 'https://diceroller-uwe7.onrender.com/roll?roll='
          if (this.in_dev){api_path =  'http://localhost:5000/roll?roll='}
          api_path = api_path.concat(dice)
          //console.log(api_path);
          var currResult = await fetch(api_path)
          .then(res => res.json())
          .then(response => response['result'])
          .catch(err => console.log(err));
          console.log([name, dice_val, currResult])
          roll_results.push([name, dice_val, currResult])
        }
        this.results.unshift([monster, roll_results])
      },
      clear(){
      this.results = []
    }
    },
    mounted() {
      this.dice_presets.unshift({'PresetName': "Normal", "Rolls": [['Attack','1d20+8'], ['Damage','3d6']]})
      console.log("Preset was mounted.")
    }
  }
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

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

.compact {
  margin-top: 4px;
  margin-bottom: 4px;
  padding: 0px;
}

.header {
  margin-top: 16px;
  margin-bottom: 8px;
  padding: 0px;
}

</style>
  