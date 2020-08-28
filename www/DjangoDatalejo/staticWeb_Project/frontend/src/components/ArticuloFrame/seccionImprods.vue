<template >
  <section >
    <div class="container-fluid"  :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
          <div class="row" style="margin:5%;" >
            <div class="col-md-3 col-md-offset-5" >
                    <h2 class='titleArticle'>{{tituloSeccion}}<br></h2>
            </div>
          </div>
          <div class="row"  >
            <div class="col-md-1" style="margin:0.5%;  ">

            </div>
            <div class="col-md-3" style="margin:0.5%;  ">
                    <h2 class='titleArticle'>{{tituloArticulo1}}</h2>
                    <div class="textArticle" align="center; margin:2%; " ><br>{{textoArticulo1}}<br>
                        <img :src="require('@/assets/' + imagenFondo1 + '')" 
                          style="border-radius:10px 10px 10px 10px;height: 70%; width: 100%; margin: 5% 0% 7% 0% ">  
                    </div>       
            </div>
            <div class="col-md-3" style="margin:0.5%;">
                    <h2 class='titleArticle'>{{tituloArticulo2}}</h2>
                    <div class="textArticle" align="justifed; margin:2%; " ><br>{{textoArticulo2}}<br>
                        <img :src="require('@/assets/' + imagenFondo2 + '')" 
                          style="border-radius:10px 10px 10px 10px;height: 100%; width: 100%;  margin: 5% 0% 7% 0% "> 
                    </div>           
            </div>
            <div class="col-md-3" style="margin:0.5%;">
                    <h2 class='titleArticle'>{{tituloArticulo3}}</h2>
                    <div class="textArticle" align="justifed; margin:2%; " ><br>{{textoArticulo3}}<br>
                        <img :src="require('@/assets/' + imagenFondo3 + '')" 
                          style="border-radius:10px 10px 10px 10px;height: 100%; width: 100%;  margin: 5% 0% 7% 0% ">      
                    </div>    
            </div>
            <div class="col-md-1" style="margin:0.5%;  ">
                
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
      tituloSeccion:{
        type: String,
        default:"titulo"
      },
      tituloArticulo1:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoArticulo1:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      imagenFondo1:{
        type: String,
        default:"product0.jpg"
      },
      tituloArticulo2:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoArticulo2:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      imagenFondo2:{
        type: String,
        default:"product1.jpg"
      },
      tituloArticulo3:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoArticulo3:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      imagenFondo3:{
        type: String,
        default:"product2.jpg"
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
.titleArticle {

  color: rgb(63,69,77);
  /*font-size: 24px;*/
  font-size: 1.5vw;
}


.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  /*font-size: 16px;*/
  font-size: 1vw;
  white-space: pre-wrap;

}

@media only screen and (max-width: 800) { 

 .textArticle{
    font-size: 5vw;
    /*font-size: 24px;*/
}
.titleArticle{
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
  padding: 4% 4% 4% 4%;
}
.contenedor-paralax{
  position: relative;
  z-index: -1;
}

.frameBack1{
  position: relative;
  background-color: #1b222c;
  z-index: -2;
}
.frameBack{
  position: relative;
  background-color: #01a39c;
    /*background-color: #05668d;*/
    /*background-color: #03dcf8;*/
    /*background-color: #2b2d42;
    color: #8d99ae;
    color: #edf2f4; */
    /*color: #02c39a;*/
  /*speed-factor:"0.5";*/
  /*direction:'down';*/
  /*sectionHeight: "170";*/
  /*width: 100%;*/
  /*height:100vh;*/
  z-index: -1;
}

.frameFront{
  position: relative;
  /*direction:'up';*/
  width: 100%;
  /*height:100%;*/
  /*height:"1600";*/
  z-index: 0;
}

/*
.big-row {
  height: 40vh;
}*/
</style>