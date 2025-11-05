<template>
    <!--History-->
    <div id="roll" v-if='results.length != 0'>
      <p class="iroll" v-for="result in results"><b>{{result[0]}}:</b> {{result[1]}}</p>
    </div>
    <p>Hello</p>
</template>
  
<script>
  export default {
    name: 'History',
    props: {
        rolls: Array
    },
    data (){
     return {
        results:[],
     }
    },
    methods: {

    },
    mounted() {

    }
  }
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
  