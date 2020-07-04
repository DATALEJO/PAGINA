<template >
  <section >
    <div class="container-fluid"  :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }"
            style="z-index: -1;">
          <div class="row "  >
            <div class="col-md-6  col-md-pull-6">
                <!--<div class="contenedor-paralax">
                      //<h1 class="parallax-title">{{textoSobreImagen}}</h1>
                      <parallax   direction='down' speed-factor="0.1" 
                          breakpoint="(min-width: 80px)" class="frameFront">
                            <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                            style="height: 100%; width: 100%; object-fit: contain">
                      </parallax> 
                </div>-->
                <div  class="frameBack"  > 
                <img :src="require('@/assets/' + imagenFondo + '')"  
                    alt="back" 
                    style="border-radius:0px 20px 20px 0px;height: 100%; width: 100%; object-fit: contain">                    
                </div>              
            </div>
            <div class="col-md-6  col-md-push-6" style="padding:100px;">
                    <h1 >{{tituloArticulo}}</h1>
                    <div class="textArticle" align="justifed" ><br>{{textoArticulo}}</div>
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


.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  font-size: 16px;

}

.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/
  z-index: -1;
  padding: 0vh;
  padding: 10px 0px 10px 0px;
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

.big-row {
  height: 40vh;
}
</style>