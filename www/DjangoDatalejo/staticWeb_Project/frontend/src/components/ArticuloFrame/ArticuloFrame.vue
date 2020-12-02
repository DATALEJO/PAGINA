<template >
  <section >
    <div class="container-fluid" :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
          <div class="row"  >
            <div class="col-md-6" style="padding:7%;">
                    <h1 class="titleArticle" style="text-align:center;" >{{tituloArticulo}}</h1>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo}}</p>
            </div>
            <div class="col-md-6">
                <div class="contenedor-paralax">
                      <!--<h1 class="parallax-title">{{textoSobreImagen}}</h1>-->
                      <!--<parallax  :direction='up' speed-factor="0.01"  
                          breakpoint="(min-width: 80px)" class="frameFront" >
                            <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                            style="height: 100%; width: 100%; object-fit: contain">
                      </parallax>  -->
                <div class="col-md-0">
                </div>
                <div class="col-md-11 col-lg-11 col-xl-11"> <!-- col-md-8 -->
                    <div class="col-md-0">
                    </div>
                    <div class="col-md-12">
                        <div  class="frameBack1"  >
                            <!--<img :src="require('@/assets/' + imagenFondo + '')"  
                                style="border-radius:10px 10px 10px 10px;height: 100%; width: 100%;margin: 20% 0% 0% 0%;"> 
                                -->
                            <img :src="require('@/assets/' + imagenFondo + '')" 
                                  style="border-radius:10px 10px 10px 10px;height: 100%; width: 100%;margin: 10% 0% 0% 0%;">                   
                          
                        </div>
                    </div>
                    <div class="col-md-0">
                    </div>
                </div>
                <div class="col-md-1 col-lg-1 col-xl-1"> <!-- col-md-4 -->
                </div>      
                </div>             
            </div>
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
        default:"este es el titulo del texto"
      },
      textoArticulo:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      textoSobreImagen:{
        type:String,
        default:"producto"
      },
      imagenFondo:{
        type: String,
        default:"medirFondo.jpg"
      },
      imagenConGamma:{
        type: String,
        default:"medir.png"
      }
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
.titleArticle{

  color: rgb(63,69,77);
  /*font-size: 24px;*/
  font-size: 2.2vw;
  text-align:justify;
}

.row .col-md-6{
  z-index: 0;
}
.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  /*font-size: 16px;*/
  font-size: 1.3vw;
  white-space: pre-wrap;
  text-align:justify;

}

@media only screen and (max-width: 800px) { 

 .textArticle{
  text-align:justify;
    font-size: 5vw;
    /*font-size: 24px;*/
}
.titleArticle{
  text-align:justify;
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
  background-image: '@/assets/fondoTodo.png';
  padding: 4% 0% 4% 0%;
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
.video{
  width: 100%;
  /*height:100vh;*/
  border-radius:10px 10px 10px 10px;
  margin: 15% 0% 0% 0%;
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

.big-row {
  height: 40vh;
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