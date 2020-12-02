<template >
  <section >
    <div class="container-fluid">
        <video class="video-bg"  
            :src="require('@/assets/' + imagenFondo0 + '')"  
            :type="video/mp4" 
            :autoplay="true"
            :loop="true">
        </video>
        <div class="text-oa">
            <h1 class="titleArticlebt"><br>{{tituloArticulo}}</h1>
            <h1 class="titleArticlebt"><br>{{tituloSubArticulo}}</h1>
            <h2 class="textArticlebt" align="justifed" >{{textoSubArticulo}}<br><br></h2>
            <h1 class="titleArticlebt">{{tituloSubArticuloA}}</h1>
            <h2 class="textArticlebt" align="justifed" >{{textoSubArticuloA}}<br><br></h2>
            <h1 class="titleArticlebt">{{tituloSubArticuloB}}</h1>
            <h2 class="textArticlebt" align="justifed" >{{textoSubArticuloB}}<br><br></h2>
            <h1 class="titleArticlebt">{{tituloSubArticuloC}}</h1>
            <h2 class="textArticlebt" align="justifed" >{{textoSubArticuloC}}<br><br><br></h2>
        </div>
    </div>
  </section>
</template>

<script>
import Parallax from "vue-parallaxy";
//import { PlyrVideo } from 'vue-plyr';

export default {
  name: 'articuloFrame',
  components: {   
       Parallax,
  //      PlyrVideo
  },
  props: {
      tituloArticulo:{
        type: String,
        default:"BENEFICIOS"
      },
      tituloSubArticulo:{
        type: String,
        default:"Decida más rápido"
      },
      textoSubArticulo:{
        type: String,
        default:"Por medio del uso de  sensores y algoritmos procesamos y analizamos los datos para que  tome mejores decisiones en el menor tiempo posible."
      },
      tituloSubArticuloA:{
        type: String,
        default:"Resuelva mejor"
      },
      textoSubArticuloA:{
        type: String,
        default:"Al combinar tecnología IoT con algoritmos de inteligencia artificial y el desarrollo de Hardware podemos adquirir nueva información con la que usted puede mejorar su capacidad de decisión."
      },
      tituloSubArticuloB:{
        type: String,
        default:"Visualice"
      },
      textoSubArticuloB:{
        type: String,
        default:"Hacemos que la información obtenida sea de fácil interpreción a través del uso de tableros de datos."
      },
      tituloSubArticuloC:{
        type: String,
        default:"Disminuya riesgos"
      },
      textoSubArticuloC:{
        type: String,
        default:"Usando vehículos no tripulados y sensores reducimos la exposición de su personal a posibles riesgos."
      },
      imagenFondo0:{
        type: String,
        default:"ima0.mp4"
      },
  }
};
</script>
<style scoped>

/*@font-face {
  font-family: 'FoundryGridnik';
  // Antes de descargar el archivo, le decimos al buscador
  //que intente buscar en local la fuente con nombre
  //Cabin, Cabin Regular o Cabin-Regular 
  src: local('FoundryGridnik'),
       local('FoundryGridnik Medium'),
       local('@assets/FoundryGridnikMedium/FoundryGridnikMedium.oft'),
       url(http://fontsgeek.com/fonts/FoundryGridnik-Bold) format('otf');
}*/
.titleArticlebt{

  /*color: rgb(63,69,77);*/
  color: white;
  /*font-size: 24px;*/
  font-size: 2.2vw;
  text-align:center;
}

.video-bg{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    overflow:hidden;
}
.text-oa{
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background:  rgb(43, 42, 42);
    z-index: 1;
    opacity: 0.85;
}
.row .col-md-4{
  z-index: 0;
}
.textArticlebt{
  /*font-size: medium;*/
  /*color: rgb(109,113,120);*/
  color: white;
  /*font-size: 16px;*/
  font-size: 1.3vw;
  white-space: pre-wrap;
  text-align:center;

}

@media only screen and (max-width: 800px) { 

 .textArticlebt{
  text-align:center;
    font-size: 5vw;
    /*font-size: 24px;*/
}
.titleArticlebt{
  text-align:center;
    font-size: 6vw;
    /*font-size: 16px*/
  }
}


.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/
  padding: 0vh;
  z-index: -1;
}
.contenedor-paralax{
  position: relative;
  z-index: -1;
}

.frameBack1{
  position: relative;
  /*background-color: #05668d;*/
  z-index: -2;
}
.frameBack{
  position: relative;
    /*background-color: #05668d;
    color: #028090;*/
    /*background-color: #1b222c;/*
    color: #8d99ae;
    color: #edf2f4; */
    /*color: #02c39a;*/
  /*speed-factor:"0.5";*/
  /*direction:'down';*/
  /*sectionHeight: "170";*/
  top: 0;
  left: 0;
  /*width: 100%;*/
  /*height:100vh;*/
  z-index: -1;
}

.frameFront{
  position: absolute;
  /*direction:'up';*/
  top: 0;
  left: 0;
  width: 100%;
  /*height:100%;*/
  z-index: 0;
  /*height:"1600";*/

}

.parallax-title {
  position: absolute;
  top: 50vh;
  left: 0;
  right: 0;
  padding: 20px;
  background: rgba(0, 0, 0, 0.315);
  color: rgb(200, 205, 221);
  text-align: center;
}

/*
@media screen and (max-width: 600px){
  .container-fluid{
    height: 150vh;
  }
}
*/
.pre{
  border: transparent;
  background-color: transparent;
}
</style>