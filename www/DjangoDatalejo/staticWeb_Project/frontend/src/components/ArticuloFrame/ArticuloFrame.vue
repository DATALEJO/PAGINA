<template >
  <section >
    <div class="container-fluid" :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }"
            style="z-index: -1;">
          <div class="row"  >
            <div class="col-md-6" style="padding:100px;">
                    <h1 class="titleArticle" >{{tituloArticulo}}</h1>
                    <div class="textArticle" align="justifed" ><br>{{textoArticulo}}</div>
            </div>
            <div class="col-md-6">
                <div class="contenedor-paralax">
                      <!--<h1 class="parallax-title">{{textoSobreImagen}}</h1>-->
                      <parallax  :direction='up' speed-factor="0.01"  
                          breakpoint="(min-width: 80px)" class="frameFront" >
                            <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                            style="height: 100%; width: 100%; object-fit: contain">
                      </parallax>  
                  <div  class="frameBack"  > 
                    <img :src="require('@/assets/' + imagenFondo + '')"  
                        style="border-radius:20px 0px 0px 20px;height: 100%; width: 100%; object-fit: contain">                    
                  </div> 
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
  font-size: 24px;
}

.row .col-md-6{
  z-index: 0;
}
.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  font-size: 16px;

}

.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/
  padding: 0vh;
  z-index: -1;
  background-image: '@/assets/fondoTodo.png';
}
.contenedor-paralax{
  position: relative;
  z-index: -1;
}
.frameBack{
  position: relative;
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
  height:100%;
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
</style>