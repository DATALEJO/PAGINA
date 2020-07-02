<template>
<!-- Navigation -->
<!--
<nav class="navbar navbar-expand-lg navbar-light bg-transparent fixed-top" role="navigation">
  <div class="container-fluid">
    <router-link class="navbar-brand"  to="/">
          <img :src="require('@/assets/logoDatalejo.png')" alt="very cool bg" width="150" height="75">
        </router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav ml-auto">
           <li class="nav-item">
            <router-link class="nav-link" to="/"><b class="color_item">Inicio</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/Sencore"><b class="color_item">Sencore</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/CadDrone"><b class="color_item">CadDrone</b></router-link>
            </li>
           <li class="nav-item">
            <router-link class="nav-link" to="/MapSafe"><b class="color_item">MapSafe</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/RetailHere"><b class="color_item">RetailHere</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/DroneFacade"><b class="color_item">DroneFacade</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/InventEye"><b class="color_item">InventEye</b></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/Contacto"><b class="color_item">Contacto</b></router-link>
            </li>
      </ul>
    </div>
  </div>
</nav>-->
<nav class="nav">
  <div class="contenedor-frontal-navbar">
        <div class="container">
            <div class="logo">
              <router-link class="navbar-brand"  to="/">
                <img :src="require('@/assets/Logo@2x.png')" alt="very cool bg" width="70" height="55">
              </router-link>
            </div>
            <div id="mainListDiv" class="main_list">
                <ul class="navlinks">
                    <li ><router-link  to="/"><a>Inicio</a></router-link></li>
                    <li ><router-link  to="/Sencore"><a>Sencore</a></router-link></li>
                    <li ><router-link  to="/CadDrone"><a>CadDrone</a></router-link></li>
                    <li ><router-link  to="/MapSafe"><a>MapSafe</a></router-link></li>
                    <li ><router-link  to="/RetailHere"><a>RetailHere</a></router-link></li>
                    <li ><router-link  to="/DroneFacade"><a>DroneFacade</a></router-link></li>
                    <li ><router-link  to="/InventEye"><a>InventEye</a></router-link></li>
                    <li ><router-link  to="/Contacto"><a>Contacto</a></router-link></li>
                    </ul>
            </div>
            <span class="navTrigger">
                <i></i>
                <i></i>
                <i></i>
            </span>
        </div>
      
    </div>
  </nav>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
//import axios from 'axios';
export default {
  name: 'Navigation', 
  mounted (){
    $('.navTrigger').click(function () {
      $(this).toggleClass('active');
      console.log("Clicked menu");
      $("#mainListDiv").toggleClass("show_list");
      $("#mainListDiv").fadeIn();
    });
    $(window).scroll(function() {
      if ($(document).scrollTop() > 50) {
        $('.nav').addClass('affix');
        console.log("OK");
      } else {
        $('.nav').removeClass('affix');
      }
    });
}
 
  /*data() {
    return {
      fields:[
        { key: 'id' },
        { key: 'nombre' },
        { key: 'descripcion' }
      ]
      , items: []
    }
  },
  
  methods: {
    getListNavbar(){
      const path = 'http://localhost:8005/api/v1.0/page/'
      axios.get(path).then((response)=>{
        this.items= response.data
      })
      .catch.log((error) => {
        console.log(error)
      })
    }
  },
  created(){
    this.getListNavbar()
  }
*/

}


 /*   $(document).on('click','.navbar-collapse.in',function(e) {
        if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
                $(this).collapse('hide');
        }
    });*/
</script>
<style >
/*.nav-collapse .dropdown-menu {
    position: relative; //### cambias el "static" por "relative"
    top: auto;
    left: auto;
    display: none;
    float: none;
    max-width: none;
    padding: 0;
    margin: 0 15px;
    background-color: transparent;
    border: none;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
    -webkit-box-shadow: none;
       -moz-box-shadow: none;
            box-shadow: none;
}*/

.spacing {
  margin-right: 10px;
}
#nav {
  overflow: hidden;
  background-color: #333;
  position: fixed; /* Set the navbar to fixed position */
  top: 10; /* Position the navbar at the top of the page */
  width: 100%; /* Full width */
}
#router-link {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.nav-item{
  font-size: large;
}
header{
  position: fixed;
  width: 100%;
  /*z-index: 1000;*/
}
/*
  .router-link-active {
    background-color: #a72a64
  }*/
@import url('https://fonts.googleapis.com/css?family=Quicksand:400,500,700');
html,
body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Quicksand", sans-serif;
    font-size: 62.5%;
    font-size: 10px;
}
/*-- Inspiration taken from abdo steif -->
/* --> https://codepen.io/abdosteif/pen/bRoyMb?editors=1100*/
.contenedor-frontal-navbar{
  z-index: 3;
}

/* Navbar section */

.nav {
    width: 100%;
    height: 65px;
    position: fixed;
    line-height: 65px;
    text-align: center;
}

.nav div.logo {
    float: left;
    width: auto;
    height: auto;
    padding-left: 0em;
}

.nav div.logo a .router-link   {
    text-decoration: none;
    color: #fff;
    font-size: 2.5rem;
}

.nav div.logo a:hover .router-link:hover{
    color: rgb(0, 92, 230);
}

.nav div.main_list {
    height: 65px;
    float: right;
}

.nav div.main_list ul {
    width: 100%;
    height: 65px;
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav div.main_list ul li {
    width: auto;
    height: 65px;
    padding: 0;
    padding-right: 3rem;
}

.nav div.main_list ul li a {
    text-decoration: none;
    color: rgb(173, 170, 170);/*color de la fuente del navbar*/
    line-height: 65px;
    font-size: 1.9rem;
    font-weight: bolder;
}

.nav div.main_list ul li a:hover {
    color: rgb(0, 100, 230);
}


/* Home section */

.home {
    width: 100%;
    height: 100vh;
    background-image: url(https://images.unsplash.com/photo-1498550744921-75f79806b8a7?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=b0f6908fa5e81286213c7211276e6b3d&auto=format&fit=crop&w=1500&q=80);
    background-position: center top;
	background-size:cover;
}

.navTrigger {
    display: none;
}

.nav {
    padding-top: 20px;
    padding-bottom: 20px;
    -webkit-transition: all 0.4s ease;
    transition: all 0.4s ease;
}


/* Media qurey section */

@media screen and (min-width: 768px) and (max-width: 1024px) {
    .container {
        margin: 0;
    }
}

@media screen and (max-width:768px) {
    .navTrigger {
        display: block;
    }
    .nav div.logo {
        margin-left: 1px;
    }
    .nav div.main_list {
        width: 100%;
        height: 0;
        overflow: hidden;
    }
    .nav div.show_list {
        height: auto;
        display: none;
    }
    .nav div.main_list ul {
        flex-direction: column;
        width: 100%;
        height: 100vh;
        right: 0;
        left: 0;
        bottom: 0;
        background-color: rgb(43, 42, 42);
        /*same background color of navbar*/
        background-position: center top;
    }
    .nav div.main_list ul li {
        width: 100%;
        text-align: right;
    }
    .nav div.main_list ul li a {
        text-align: center;
        width: 100%;
        font-size: 3rem;
        padding: 20px;
    }
    .nav div.media_button {
        display: block;
    }
}


/* Animation */
/* Inspiration taken from Dicson https://codemyui.com/simple-hamburger-menu-x-mark-animation/ */

.navTrigger {
    cursor: pointer;
    width: 30px;
    height: 25px;
    margin: auto;
    position: absolute;
    right: 30px;
    top: 0;
    bottom: 0;
}

.navTrigger i {
    background-color: #fff;
    border-radius: 2px;
    content: '';
    display: block;
    width: 100%;
    height: 4px;
}

.navTrigger i:nth-child(1) {
    -webkit-animation: outT 0.8s backwards;
    animation: outT 0.8s backwards;
    -webkit-animation-direction: reverse;
    animation-direction: reverse;
}

.navTrigger i:nth-child(2) {
    margin: 5px 0;
    -webkit-animation: outM 0.8s backwards;
    animation: outM 0.8s backwards;
    -webkit-animation-direction: reverse;
    animation-direction: reverse;
}

.navTrigger i:nth-child(3) {
    -webkit-animation: outBtm 0.8s backwards;
    animation: outBtm 0.8s backwards;
    -webkit-animation-direction: reverse;
    animation-direction: reverse;
}

.navTrigger.active i:nth-child(1) {
    -webkit-animation: inT 0.8s forwards;
    animation: inT 0.8s forwards;
}

.navTrigger.active i:nth-child(2) {
    -webkit-animation: inM 0.8s forwards;
    animation: inM 0.8s forwards;
}

.navTrigger.active i:nth-child(3) {
    -webkit-animation: inBtm 0.8s forwards;
    animation: inBtm 0.8s forwards;
}

@-webkit-keyframes inM {
    50% {
        -webkit-transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(45deg);
    }
}

@keyframes inM {
    50% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(45deg);
    }
}

@-webkit-keyframes outM {
    50% {
        -webkit-transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(45deg);
    }
}

@keyframes outM {
    50% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(45deg);
    }
}

@-webkit-keyframes inT {
    0% {
        -webkit-transform: translateY(0px) rotate(0deg);
    }
    50% {
        -webkit-transform: translateY(9px) rotate(0deg);
    }
    100% {
        -webkit-transform: translateY(9px) rotate(135deg);
    }
}

@keyframes inT {
    0% {
        transform: translateY(0px) rotate(0deg);
    }
    50% {
        transform: translateY(9px) rotate(0deg);
    }
    100% {
        transform: translateY(9px) rotate(135deg);
    }
}

@-webkit-keyframes outT {
    0% {
        -webkit-transform: translateY(0px) rotate(0deg);
    }
    50% {
        -webkit-transform: translateY(9px) rotate(0deg);
    }
    100% {
        -webkit-transform: translateY(9px) rotate(135deg);
    }
}

@keyframes outT {
    0% {
        transform: translateY(0px) rotate(0deg);
    }
    50% {
        transform: translateY(9px) rotate(0deg);
    }
    100% {
        transform: translateY(9px) rotate(135deg);
    }
}

@-webkit-keyframes inBtm {
    0% {
        -webkit-transform: translateY(0px) rotate(0deg);
    }
    50% {
        -webkit-transform: translateY(-9px) rotate(0deg);
    }
    100% {
        -webkit-transform: translateY(-9px) rotate(135deg);
    }
}

@keyframes inBtm {
    0% {
        transform: translateY(0px) rotate(0deg);
    }
    50% {
        transform: translateY(-9px) rotate(0deg);
    }
    100% {
        transform: translateY(-9px) rotate(135deg);
    }
}

@-webkit-keyframes outBtm {
    0% {
        -webkit-transform: translateY(0px) rotate(0deg);
    }
    50% {
        -webkit-transform: translateY(-9px) rotate(0deg);
    }
    100% {
        -webkit-transform: translateY(-9px) rotate(135deg);
    }
}

@keyframes outBtm {
    0% {
        transform: translateY(0px) rotate(0deg);
    }
    50% {
        transform: translateY(-9px) rotate(0deg);
    }
    100% {
        transform: translateY(-9px) rotate(135deg);
    }
}

.affix {
    padding: 0;
    background-color:rgb(27,34,44);/*color navbar de la barra al bajar*/
}






.myH2 {
	text-align:center;
	font-size: 4rem;
}
.myP {
	text-align: justify;
	padding-left:15%;
	padding-right:15%;
	font-size: 20px;
}
@media all and (max-width:700px){
	.myP {
		padding:2%;
	}
}
</style>

