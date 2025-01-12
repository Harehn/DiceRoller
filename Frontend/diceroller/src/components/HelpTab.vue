<template>
    <h1>Help</h1>
    <h2>Summary</h2>
    <p>This app was made because I needed a quick easy way to store and roll homebrew rolls for DND.
        This provides a quick easy way to roll my monster attacks. <br>
        This way multiple rolls such as attack, damage multi-attacks will be rolled much faster and easier.
    </p>

    <h2>What do the strings mean</h2>
    <p><b>Formatting.</b> The string 3d10 refers to 3 dices that have 10 faces each (from 1 to 10). The output of rolling will be the sum of the 3 dices.
        3d10 + 2 means adding 2 to the sum of the rolled dices.    
    </p>
    <p><b>Summary.</b> XdY + Z ==> X Y-sided dice rolled and add Z to the final result.    
    </p>

    <h2>Use</h2>
    <p>The home tab allows for single rolls to be made. Beware that the history clears as you change tabs and is not cached.</p>
    <p>The preset tab allows you to store presets ie sets of dices to roll.</p>


    <h2>Issues</h2>
    <p>The presets are stored locally and sometimes that may have an issue and be cleared automatically.</p>
    <input type='button' style="float: left;" value='Clear LocalStorage Manually' @click=clear>
    <br>
    <p>The Backend may take a little while to wake up and all the pending rolls might appear all at once.</p>
    <p>Not all incorrect strings are caught at the input sanitation or the checks at the Backend.</p>
    <p>If issues persist, contact hkaundun@gmail.com. </p>

    <h2>Further Development</h2>
    <p>I intend to add a possible download for the history and import/export of presets.</p>
    <p>However, this can be considered a version 1.0 and further development will have to wait.</p>
    <p>Website background image seems to interfere with reading the html elements. I will find a way to properly blend the image.</p>

    
</template>
  
<script>
  export default {
    name: 'HelpTab',
    data (){
     return {

     }
    },
    methods: {
        clear(){
            localStorage.clear();
        }
    },
    mounted() {
      console.log("About was mounted.")
    }
  }
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h2 {
    text-align: left;
    margin-left: 20px;
    margin-right: 20px;
}

p {
    text-align: left;
    margin-left: 20px;
    margin-right: 20px;
}


</style>
  