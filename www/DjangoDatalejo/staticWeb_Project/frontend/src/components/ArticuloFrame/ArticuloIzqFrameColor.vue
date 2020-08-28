<template >
  <section >
    <div class="container-fluid" style="z-index: -1;">
          <div class="row "  >
            <div class=" col-md-6 col-md-push-6" style="padding: 5%;" ><!--inicia a la derecha y baja--> 
                    <h1 class="titleArticle"><br>{{tituloArticulo}}</h1>
                    <h1 class="titleArticle"><br><br>{{tituloSubArticulo}}</h1>
                    <h2 class="textArticle" align="justifed" >{{textoSubArticulo}}<br><br></h2>
                    <h1 class="titleArticle">{{tituloSubArticuloA}}</h1>
                    <h2 class="textArticle" align="justifed" >{{textoSubArticuloA}}<br><br></h2>
                    <h1 class="titleArticle">{{tituloSubArticuloB}}</h1>
                    <h2 class="textArticle" align="justifed" >{{textoSubArticuloB}}<br><br></h2>
                    <h1 class="titleArticle">{{tituloSubArticuloC}}</h1>
                    <h2 class="textArticle" align="justifed" >{{textoSubArticuloC}}<br><br><br></h2>
            </div>
            <div class=" col-md-6 col-md-pull-6"  style="padding: 1%; " ><!--inicia a la izq y sube-->
                <div class="col-md-3">
                </div>
                <div class="col-md-6">
                <h1 class="parallax-title">{{textoSobreImagen}}</h1>
                <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                      style="height: 100%; width: 100%; object-fit: contain; padding: 20% 0% 0% 0%;">
                </div>
                <div class="col-md-3">
                </div>
            </div>
          </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'articuloFrame',
  props: {
      tituloArticulo:{
        type: String,
        default:"Titulo"
      },
      tituloSubArticulo:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoSubArticulo:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      tituloSubArticuloA:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoSubArticuloA:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      tituloSubArticuloB:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoSubArticuloB:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      tituloSubArticuloC:{
        type: String,
        default:"este es el titulo del texto"
      },
      textoSubArticuloC:{
        type: String,
        default:"esta es la historia del texto para las referencias de toda la vida"
      },
      textoSobreImagen:{
        type:String,
        default:"producto"
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
.textArticle{
  /*font-size: 16px;*/
  font-size: 1vw;
  font-weight: normal;
  color: white;
  white-space: pre-wrap;
}
.titleArticle{
  /*font-size: 24px;*/
  font-size: 1.2vw;
   font-weight: bolder;
   color: white;
}

@media only screen and (max-width: 800px) { 

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
  background-color: rgb(27,34,44);
  /*margin: 50px 0px 50px 0px; */
  /*width: 100%;*/
  padding: 10px 0px 10px 0px;
}


.parallax-title {
  position: absolute;
  top: 50vh;
  left: 0;
  right: 0;
  padding: 20px;
  /*background: rgba(0, 0, 0, 0.315);*/
  color: rgb(200, 205, 221);
  text-align: center;
}

</style>