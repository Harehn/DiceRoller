<template>
    <h1>About</h1>
    <h2>Summary</h2>
    <p>This app was made because I needed a quick easy way to store and roll homebrew rolls for DND.
        This provides a quick easy way to roll my monster attacks.
    </p>
    <h2>Website Icon</h2>
    <p>dice clipart PNG Designed By 588ku from https://pngtree.com/freepng/red-dice_5420638.html?sol=downref&id=bef</p>
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
  