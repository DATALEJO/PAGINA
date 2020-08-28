<template >
  <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
    <div class="container-fluid" >
      <div class="row">
        <div class="col-md-12">
          <div class="interbox" >
            <div class="textArticle"  >{{articuloInter}}</div>
          </div>
        </div>
      </div>
    </div>   
  </section>
</template> 

<script>
export default {   
  name: 'articuloIntermedio',
  props: {
      articuloInter:{
        type: String,
        default:"que chevere"
    },
  }
};
</script>
<style scoped>


.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/  
  padding: 3% 5% 3% 5%;
}

.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  /*font-size: 16px;*/
  font-size: 1.3vw;
  text-align: justify;

}

@media only screen and (max-width: 800) { 

 .textArticle{
  text-align:justify;
    font-size: 6vw;
    /*font-size: 24px;*/
  }
}
</style>
