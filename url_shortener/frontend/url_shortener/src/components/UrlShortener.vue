<template>
  <div>
    <h1>Último Shortlink: {{ value }}</h1>
    <form @submit.prevent="updateCurrentShortlink">
      <input v-model="new_value" placeholder="Novo link" />
      <button type="submit">update</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "UrlShortener",
  data: () => {
    return {
      value: null,
    };
  },
  methods: {
    async getCurrentShortlink() {
      let response = await fetch("http://localhost:8000/shortlink", {
        method: "get",
      });
      if (response.ok) {
        let resp = await response.json();
        this.value = resp.shortlink.url;
        return;
      }
      this.value = "could not load from server";
      return;
    },
    async updateCurrentShortlink() {
      if (this.new_value === null) {
        return;
      } // checagem para valores null e 0

      fetch("http://localhost:8000/shortlink", {
        method: "post",
        body: JSON.stringify({
          url: this.new_value,
        }),
        headers: { "Content-type": "application/json" },
      })
        .then(() => this.refreshPage())
        .catch((err) => console.error(err));
      return;
    },
    refreshPage() {
      location.reload();
    },
  },
  mounted() {
    this.getCurrentShortlink();
  },
};
</script>