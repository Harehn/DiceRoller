<template>
    <h1>About</h1>
    <h2>Summary</h2>
    <p>This app was made because I needed a quick easy way to store and roll homebrew rolls for DND.
        This provides a quick easy way to roll my monster attacks.
    </p>

    <h2>How to use this website</h2>
    <p><b>Formatting.</b> The formatting of the dice rolls follow the conventional formatting of Wizards of the coasts.
    Eg 3d6+2 or 3d10. White space is removed before sending to the backend.
    3 d 6 + 2, 3d6 + 2 and 3d6+2 will all send the same request. 
    </p>

    <h2>Resources</h2>

    <h2>Technical</h2>
    <p><b>Github</b> The code of this website (Frontend and Backend) is hosted on github <a href="https://github.com/Harehn/DiceRoller" target="_blank">here</a></p>
    <p><b>Hosting</b>The backend of the code is hosted on Render <a href="https://diceroller-uwe7.onrender.com" target="_blank">here</a>
    The frontend is hosted on Render <a href="https://dicerollers.onrender.com" target="_blank">here</a>
    </p>
    <p><b>Technologies</b>The backend app was made using Flask and the frontend uses Vue js</p>


    
</template>
  
<script>
  export default {
    name: 'About',
    data (){
     return {

     }
    },
    methods: {
      sample() {
      },
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
  