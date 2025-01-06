<template>
    <h1>Preset</h1>
    <table id="preset_table">
      <tr>
        <th>Preset Name(Monster)</th>
        <th>Dice to roll</th>
        <th></th>
        <th></th>
      </tr>
      <tr v-for="preset in dice_presets">
        <td>{{ preset["PresetName"] }}</td>
        <td>
          <p v-for="roll in preset['Rolls']">{{ roll[0]}}: {{ roll[1] }}</p>
        </td>
        <td>
          <input type='button' value='Roll' @click='roll_preset(preset)'>
        </td>
        <td>
          <input type='button' value='delete' @click='preset_remove(preset)'>
        </td>
      </tr>
      <tr>
        <td><input type='text' id='preset_name' name='preset_name' @keyup.enter="makePreset"></td>
        <td>
          <div v-for="i in dice" class="dice_roll_div">
            <label>Roll Name:</label>
            <input type='text' class='dice_roll_name' name='dice_roll_name'  @keyup.enter="makePreset">
            <label>Dice to roll:</label>
            <input type='text' class='dice_roll_dice' name='dice_roll_dice'  @keyup.enter="makePreset">
          </div>
          <span class="add" @click="dice=Math.max(dice+1, 1)">+</span>
          <span class="add" @click="dice=Math.max(dice-1, 1)">-</span>
        </td>
        <td>
          <input type='button' value='Add Preset' @click='makePreset'>
        </td>
        <td>
          <input type='button' value='Clear Text' @click=''>
        </td>
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
      results:[],
      in_dev: false,
      dice: 2,
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
          console.log(api_path);
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
    },
      makePreset(){
        var new_preset = {};
        new_preset['PresetName'] = document.getElementById("preset_name").value;
        
        var roll_names = (Array.from(document.getElementsByClassName("dice_roll_name")).map((v) => v.value));
        var roll_dices = (Array.from(document.getElementsByClassName("dice_roll_dice")).map((v) => v.value));
        var roll_array = [];
        for (var i = 0; i < roll_names.length; i++){
          roll_array.push([roll_names[i], roll_dices[i]])
        }
        new_preset['Rolls'] = roll_array;
        console.log(new_preset);
        this.dice_presets.unshift(new_preset);
        //Putting this here instead of in 'watch' because it was not updating as it should
        localStorage.dice_presets = JSON.stringify(this.dice_presets); 
      },
      preset_remove(preset){
        this.dice_presets = this.dice_presets.filter(item => item !== preset);
        localStorage.dice_presets = JSON.stringify(this.dice_presets);
      }
    },
    mounted() {
      //this.dice_presets.unshift({'PresetName': "Normal", "Rolls": [['Attack','1d20+8'], ['Damage','3d6']]})
      //https://stackoverflow.com/a/58475472/28974846
      if (process.env.NODE_ENV == 'development'){
        this.in_dev = true;
        console.log("App was opened in DEVELOPMENT");
      }else{
        console.log("App was opened in PRODUCTION");
      }
      console.log("Preset was mounted.")
      if (localStorage.dice_presets){
        try{
          this.dice_presets = JSON.parse(localStorage.dice_presets);
        }catch{
          localStorage.clear();
        }
        
      }
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

/*https://www.w3schools.com/css/css_table.asp */
#preset_table {
  /* font-family: Arial, Helvetica, sans-serif; */
  border-collapse: collapse;
  width: 100%;
  max-width: 800px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 4px;
  margin-bottom: 4px;
  padding: 0px;
}

#preset_table td, #preset_table th {
  border: 1px solid #ddd;
  padding: 8px;
}

#preset_table tr:nth-child(even){background-color: #f2f2f2;}

#preset_table tr:hover {background-color: #ddd;}

#preset_table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #3a3a9a;
  color: white;
}

.dice_roll_name, .dice_roll_dice {
 width: 90px;
}

label {
  margin-left: 5px;
  margin-right: 3px;
}

#dice_roll_div {
  display: block;
}

.add {
    display: inline-block;
    text-align: center;
    background-color: grey;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    font-size: 14px;
    line-height: 26px;
    cursor: default;
    font-weight: bold;
    color:#fff;
    margin-top: 5px;
    margin-left: 5px;
}


</style>
  