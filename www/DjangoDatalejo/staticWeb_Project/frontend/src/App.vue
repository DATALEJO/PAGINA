<template>

  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style  scoped>

@font-face {
    font-family: 'Moscow';
    font-stretch: normal;
    src: url(~@/assets/fonts/Moscow-Normal.otf) format('font-opentype');
    font-weight: medium;
    font-style: normal;
  } ; 

  @font-face {
    font-family: 'FoundryGridnik';
    font-stretch: normal;
    src: url(~@/assets/fonts/FoundryGridnik-Medium.otf) format('font-opentype');
    font-weight: medium;
    font-style: normal;
  };
  
  @font-face {
    font-family: 'honor-medium-1e19';
    font-stretch: normal;
    src: url(~@/assets/fonts/honor-medium-1e19.ttf) format('ttf');
    font-weight: medium;
    font-style: normal;
  };
#app {
  /*font-family: honor-medium-1e19;*/
  /*font-family: FoundryGridnik;*/
  /*font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;*/
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  /*font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;*/
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}

</style>
