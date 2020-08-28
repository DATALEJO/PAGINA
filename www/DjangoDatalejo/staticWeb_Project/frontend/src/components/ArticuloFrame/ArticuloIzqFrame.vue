<template >
  <section >
    <div class="container-fluid"  :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
          <div class="row"  >
            <div class="col-lg-6 col-lg-push-6 " style="padding:5%;" ><!--inicia a la derecha y baja-->
                    <h1 class="titleArticle">{{tituloArticulo}}</h1>
                    <div class="textArticle"  ><br>{{textoArticulo}}</div>
            </div>
            <div class="col-lg-6 col-lg-pull-6 "><!--inicia a la izq y sube-->
                <!--<div class="contenedor-paralax">
                      //<h1 class="parallax-title">{{textoSobreImagen}}</h1>
                      <parallax   direction='down' speed-factor="0.1" 
                          breakpoint="(min-width: 80px)" class="frameFront">
                            <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                            style="height: 100%; width: 100%; object-fit: contain">
                      </parallax> 
                </div>-->
                <div class="col-md-1">
                </div>
                <div class="col-md-11">
                    <div class="col-md-0">
                    </div>
                    <div class="col-md-12">
                        <div  class="frameBack1" > 
                          <img :src="require('@/assets/' + imagenFondo + '')" 
                                  style="border-radius:10px 10px 10px 10px;height: 100%; width: 100%;margin: 10% 0% 0% 0%;">                   
                          </div> 
                    </div>
                    <div class="col-md-0">
                    </div>
                </div>
                <div class="col-md-0">
                </div>        
              </div>
        </div>
    </div>
  </section>
</template>

<script>
import Parallax from "vue-parallaxy";
export default {
  name: 'articuloFrame',
  components: {   
       Parallax    
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
  font-size: 2.2vw;
  text-align:justify;
}


.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  /*font-size: 16px;*/
  font-size: 1.3vw;
  white-space: pre-wrap;
  text-align:justify;

}

@media only screen and (max-width: 800) { 

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
  z-index: -1;
  /*padding: 0vh;*/
  padding: 4% 0% 4% 0%;
}
.contenedor-paralax{
  position: relative;
  z-index: -1;
}

.frameBack1{
  position: relative;
  /*background-color: #1b222c;*/
  z-index: -2;
}
.frameBack{
  position: relative;
  /*background-color: #05668d;*/
    /*background-color: #05668d;*/
    /*background-color: #03dcf8;*/
    /*background-color: #2b2d42;
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
  /*height:"1600";*/
  z-index: 0;
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
.big-row {
  height: 40vh;
}*/
</style>