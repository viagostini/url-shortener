<template>
  <div class="flex-container">
    <div>
      <form @submit.prevent="createShortlink">
        <input v-model="new_value" placeholder="Paste a link" />
        <button type="submit">Create Shortlink</button>
      </form>
      <h1>Shortlink: {{ value }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "UrlShortener",
  data: () => {
    return {
      value: null,
      new_value: null,
    };
  },
  methods: {
    async createShortlink() {
      if (this.new_value === null) {
        return;
      }
      fetch("http://localhost:8000/shortlink", {
        method: "post",
        body: JSON.stringify({
          url: this.new_value,
        }),
        headers: { "Content-type": "application/json" },
      })
        .then((response) => this.displayShortlink(response))
        .catch((err) => console.error(err));
      return;
    },
    async displayShortlink(response) {
      let res = await response.json();
      this.value = res.shortlink;
      this.new_value = "";
      console.log(res);
    },
  },
};
</script>