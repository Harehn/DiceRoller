<template>
    <div class="popup" @click="sample()"><p class="question"></p>
    <span class="popuptext" id="myPopup">{{ help_msg }}</span>
    </div> 
</template>
  
<script>
  export default {
    name: 'Help',
    props: {
      help_msg: String
    },
    data (){
     return {
      popped:false
     }
    },
    methods: {
      sample() {
        var popup = document.getElementById("myPopup");
        popup.classList.toggle("show");
      },
    },
    mounted() {
      console.log("Help was mounted.")
    }
  }
</script>
  
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
   /* Popup container */
.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

/* The actual popup (appears on top) */
.popup .popuptext {
  visibility: hidden;
  width: 320px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px 0;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -160px;
}

/* Popup arrow */
.popup .popuptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

/* Toggle this class when clicking on the popup container (hide and show the popup) */
.popup .show {
  visibility: visible;
  -webkit-animation: fadeIn 1s;
  animation: fadeIn 1s
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity:1 ;}
}

.question::before{
    content:'?';
    font-weight: bold;
    color:#fff;
}

.question{
    display: inline-block;
    text-align: center;
    background-color: grey;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    font-size: 14px;
    line-height: 26px;
    cursor: pointer;
}

</style>
  