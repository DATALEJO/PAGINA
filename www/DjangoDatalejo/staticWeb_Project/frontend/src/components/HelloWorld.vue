<template>
    <div class="contenedor-todo">
    <paralax_dl></paralax_dl>
    <div >
      <articuloFrame  
        v-bind:tituloArticulo= "title0" 
        v-bind:textoArticulo= "article0" 
        v-bind:textoSobreImagen= "textimg0"
        v-bind:imagenConGamma= "imagenConGamma0"
        v-bind:imagenFondo= "imagenFondo0"
      />
    </div>
    <div class="frame-classic-short">
      <articuloIntermedio 
        v-bind:articuloInter= "articuloInter0"
      />
    </div>
    <div class="frame-classic">
        <articuloImaTresCols  
            v-bind:imagenConGamma= "imagenConGamma1" 
            v-bind:tituloSubArticuloA= "tituloSubArticuloA0" 
            v-bind:textoSubArticuloA= "textoSubArticuloA0"
            v-bind:textoSubArticuloB= "textoSubArticuloB0"
            v-bind:textoSubArticuloC= "textoSubArticuloC0"
            v-bind:imagenSubArticuloA= "imagenSubArticuloA0"
            v-bind:imagenSubArticuloB= "imagenSubArticuloB0"
            v-bind:imagenSubArticuloC= "imagenSubArticuloC0"
        />
    </div>
    <div class="frame-classic-long">
      <articuloIzqFrameColor 
        v-bind:tituloArticulo= "titleArt"
        v-bind:tituloSubArticulo= "title2" 
        v-bind:textoSubArticulo= "article2" 
        v-bind:tituloSubArticuloA= "title21" 
        v-bind:textoSubArticuloA= "article21"
        v-bind:tituloSubArticuloB= "title22" 
        v-bind:textoSubArticuloB= "article22" 
        v-bind:tituloSubArticuloC= "title23" 
        v-bind:textoSubArticuloC= "article23"  
        v-bind:textoSobreImagen= "textimg2"
        v-bind:imagenConGamma= "imagenConGamma2"
        v-bind:color= "imagenFondo2"
      />
    </div>
    <router-link class="frame-classic" to="/Contactenos">
      <articuloIzqFrame  
        v-bind:tituloArticulo= "title3" 
        v-bind:textoArticulo= "article3" 
        v-bind:textoSobreImagen= "textimg3"
        v-bind:imagenConGamma= "imagenConGamma3"
        v-bind:imagenFondo= "imagenFondo3"
      />
    </router-link>
    <div class="frame-classic-short">
      <articuloIntermedio 
        v-bind:articuloInter= "articuloInter1"
      />
    </div>
    <router-link class="frame-classic" to="/Contacto">
       <seccionProductos
        v-bind:tituloSeccion= "title4"
        v-bind:tituloArticulo1= "titleArticle1"
        v-bind:textoArticulo1= "textArticle1"
        v-bind:imagenFondo1= "imagesection41"
        v-bind:tituloArticulo2= "titleArticle2"
        v-bind:textoArticulo2= "textArticle2"
        v-bind:imagenFondo2= "imagesection42"
        v-bind:tituloArticulo3= "titleArticle3"
        v-bind:textoArticulo3= "textArticle3"
        v-bind:imagenFondo3= "imagesection43"
       />
    </router-link>
    <div>
      <lowerBanner />
    </div>
  </div>
</template>

<script>
import paralax_dl from '@/components/ParalaxVue/ParalaxVue.vue';
import articuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import articuloIzqFrame from '@/components/ArticuloFrame/ArticuloIzqFrame.vue';
import articuloIzqFrameColor from '@/components/ArticuloFrame/ArticuloIzqFrameColor.vue';
import lowerBanner from '@/components/ArticuloFrame/LowerBanner.vue';
import articuloIntermedio from '@/components/ArticuloIntermedio/ArticuloIntermedio.vue';
import articuloImaTresCols from '@/components/ArticuloFrame/ArticuloImaTresCols.vue';
import seccionProductos from '@/components/ArticuloFrame/seccionImprods.vue';

export default {
  components: {
    paralax_dl,
    articuloFrame,
    articuloIntermedio,
    articuloImaTresCols,
    articuloIzqFrameColor,
    articuloIzqFrame,
    articuloFrame,
    seccionProductos,
    lowerBanner
  },
  data(){
    return {
      title0:'Datos en la nube, Información disponible',
      article0:'Datalejo es una empresa enfocada en capturar, procesar y '+
              'analizar datos  usando como fuente sensores, tecnologías IoT “Internet Of Things” y'+
              ' algoritmos de inteligencia artificial creando tableros de resumenes orientados a la '+
              'toma de decisiones, con soluciones asequibles en costo. La captura de datos se realiza '+
              'usando vehículos no tripulados o desarrollando  hardware a la medida.',
      textimg0: 'Sencore',
      imagenConGamma0:"quehacemos.png",
      imagenFondo0:"ImagenQueHacemos.jpeg",
      
      articuloInter0:'Trabajamos con pequeñas  medianas y grandes empresas asesorando de forma personalizada '+
                    'sus necesidades para llegar a una solución conjunta. Con nuestros productos y servicios '+
                    'impulsamos su transformación digital. ',
      
      tituloSubArticuloA0: '' ,
      textoSubArticuloA0: 'Sensamos para optimizar sus costos de operación.',
      textoSubArticuloB0: 'Capturamos datos y de esta forma podrá ampliar su capacidad de decisión.',
      textoSubArticuloC0: 'Generamos reportes que permiten tomar decisiones en el menor tiempo posible.',
      imagenConGamma1: "ImagenServicios1.png" ,
      imagenSubArticuloA0:"sensor.png",
      imagenSubArticuloB0:"report.png",
      imagenSubArticuloC0:"seo-report.png",

      titleArt:"BENEFICIOS",
      title2:'Decida más rápido',
      article2:'Por medio del uso de  sensores y algoritmos procesamos y analizamos los datos para que  tome mejores decisiones en el menor tiempo posible.',
      title21:'Resuelva mejor',
      article21:'Al combinar tecnología IoT con algoritmos de inteligencia artificial y el desarrollo de Hardware podemos adquirir nueva información con la que usted puede mejorar su capacidad de decisión.',
      title22 :'Visualice',
      article22:'Hacemos que la información obtenida sea de fácil interpreción a través del uso de tableros de datos.',
      title23 : 'Disminuya riesgos',
      article23:'Usando drones y sensores reducimos la exposición de su personal a posibles riesgos.',
      textimg2: ' ',
      imagenConGamma2:"LogIllo.png",
      imagenFondo2:"rgb(63,69,77)",

      title3:'Nosotros',
      articuloInter1:'Estamos comprometidos en impulsar  la transformación de las organizaciones al paradigma de la industria 4.0 para promover nuevos modelos de negocio y así, hacer más competitivas a las  empresas.',
      textimg3: 'CapDrone',
      imagenConGamma3:"Nosotros.png",
      imagenFondo3:"ImagenNosotros.png",

      article3:'Datalejo S.A.S. esta conformada por un grupo de ingenieros con más de 10 años de experiencia en áreas relacionadas con uso de sensores, diseño de hardware, construcción de soluciones firmware-software, análisis de datos y creación de dashboards orientados a la inteligencia de negocio.',

      title4: 'Últimos productos',
      titleArticle1: 'Hardware medición temperatura',
      textArticle1: 'con este hardware podemos medir la temperatura sin tener contacto con el dispositivo y sin necesidad de tener a una persona operandolo',
      imagesection41 : 'product0.jpeg',
      titleArticle2: 'Aplicación Control Covid',
      textArticle2: 'Con esta app podemos asociar la temperatura de las personas con su numero de identificación',
      imagesection42 : 'product1.jpeg',
      titleArticle3: 'Generación de reportes App',
      textArticle3: 'Permite sacar reportes de la información recogida por nuestras apps y generar reportes ',
      imagesection43 : 'product2.jpeg',
}
  }


}
</script>

<style>
a:link
{
text-decoration:none;
  color: rgb(63,69,77);
}
.contenedor-frontal-navbar{
  z-index: 1;
}
.contenedor-todo{
  z-index: 0;
}


/*color subtitulos (63,69,77)
Color letra  general : (109,113,120) 16px*/

/*
.frame-classic{
    height: 95vh;
}

.frame-classic-long{
    height: 100vh;
}
.frame-classic-short{
    height: 45vh;
}*/
</style>
