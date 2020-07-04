<template >
  <section >
        <div class="container-fluid" :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
            <div class="row "  >
                <div class="col-md-6">
                    <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                           style="border-radius:0px 20px 20px 0px; height: 100%; width: 100%; object-fit: contain ">
                    </div>
                <div class="col-md-6" >
                    <h1 class="titleArticle"><br><br>{{tituloSubArticuloA}}<br><br><br></h1>
                    <div class="row "  >
                        <div class="col-4" >
                            <div align="center">
                              <img  :src="require('@/assets/' + imagenSubArticuloA + '')" alt="front" 
                                     style="height: 50%; width: 50%; object-fit: contain">
                            </div>
                            <h2 class="textArticle" align="justifed" ><br><br>{{textoSubArticuloA}}<br></h2>
                        </div>
                        <div class="col-4" >
                            <div align="center">
                              <img  :src="require('@/assets/' + imagenSubArticuloB + '')" alt="front"
                                     style="height: 50%; width: 50%; object-fit: contain ">
                            </div>
                            <h2 class="textArticle" align="justifed" ><br><br>{{textoSubArticuloB}}<br></h2>
                        </div>
                        <div class="col-4" >
                            <div align="center">
                              <img  :src="require('@/assets/' + imagenSubArticuloC + '')" alt="front" 
                                     style="height: 50%; width: 50%; object-fit: contain ">
                            </div>
                            <h2 class="textArticle" align="justifed" ><br><br>{{textoSubArticuloC}}<br></h2>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
  name: 'articuloImaTresCols',
  props: {
      imagenConGamma:{
        type: String,
        default:"imagenBanner.png"
      },
      tituloSubArticuloA:{
        type: String,
        default:"PRODUCTOS"
      },
      textoSubArticuloA:{
        type: String,
        default:"AWS"
      },
      textoSubArticuloB:{
        type: String,
        default:"Quickstarts"
      },
      textoSubArticuloC:{
        type: String,
        default:"Quickstarts"
      },      
      imagenSubArticuloA:{
        type: String,
        default:"imagenBanner.png"
      },    
      imagenSubArticuloB:{
        type: String,
        default:"imagenBanner.png"
      },    
      imagenSubArticuloC:{
        type: String,
        default:"imagenBanner.png"
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
.textArticle{
  font-size: 14px;
  color: rgb(109,113,120);
   font-weight: normal;
}
.titleArticle{
   font-size: small;
   font-weight: bold;
   color: black;
   text-align: center;
}

.container-fluid{
  position: relative;
  z-index: -1;
  /*height: 500px;*/
  /*background-color: rgb( 26, 78, 187);*/
  /*width: 100%;*/
  padding: 10px 0px 10px 0px;
}


</style>