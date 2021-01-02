<template>
  <UrlShortener />
</template>

<script>
import UrlShortener from "./components/UrlShortener";

export default {
  name: "App",
  components: {
    UrlShortener,
  },
};
</script>

<style>
html,
body {
  height: 100%;
}
body {
  margin: 0;
  background-color: #fffafa;
}

.btn {
  margin-left: 10px;
}

h1 {
  margin-top: 10px;
}

.flex-container {
  height: 100%;
  padding: 0;
  margin: 0;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
