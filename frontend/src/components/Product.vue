<template>
  <div class="p-4 border-black border-solid rounded-md border-2">
    <div
      class="w-full h-96"
      :style="{
        backgroundImage: 'url(' + 'http://localhost:5000/img/' + product.img + ')',
        'background-size': 'cover',
      }"
    ></div>

    <div class="text-lg to-blue-800 relative mt-1 w-full sm:flex sm:flex-col">
      <h3 class="p-1">{{ name }}</h3>
      <span class="sm:float-left md:absolute left-0 bottom-0"
        >Price: {{ product.price }}</span
      >
      <div class="flex sm:order-last md:mx-auto justify-center">
        <button
          class="rounded-full w-8 h-8"
          :disabled="count == 0"
          :class="[count == 0 ? 'bg-red-200' : 'bg-red-400']"
          @click="removeFromBasket()"
        >
          -
        </button>
        <span class="inline-block w-8">{{ count }}</span>
        <button
          class="rounded-full w-8 h-8"
          :disabled="count == quantity"
          :class="[count == quantity ? 'bg-green-200' : 'bg-green-400']"
          @click="addToBasket()"
        >
          +
        </button>
      </div>

      <span
        class="sm:inline sm:text-center md:absolute right-0 bottom-0 text-right"
        >{{ quantity - count }} item left</span
      >
    </div>
  </div>
</template>

<script lang="ts">
import { AxiosStatic } from "axios";
import { ref, defineComponent, inject, onBeforeMount } from "vue";
export default defineComponent({
  name: "Product",
  props: {
    product_id: {
      type: Number,
      default: 1,
    },
    quantity: {
      type: Number,
      default: 0,
    },
  },
  // emits: ["basketUpdate"],
  setup: (props, { emit }) => {
    const axios: AxiosStatic = inject("$axios") as AxiosStatic;
    const count = ref(0);
    const product = ref({
      name: "no name",
    });

    onBeforeMount(async () => {
      product.value = await getProductById(axios, props.product_id);
    });

    const addToBasket = async () => {
      if (count.value == props.quantity) {
        return;
      }
      count.value++;
      emit("basketUpdate", props.product_id, count.value, product.value.name);
    };

    const removeFromBasket = async () => {
      if (count.value == 0) {
        return;
      }
      count.value--;
      emit("basketUpdate", props.product_id, count.value, product.value.name);
    };

    return { product, count, addToBasket, removeFromBasket, onBeforeMount, axios };
  },
});

const getProductById = async (axios: AxiosStatic, product_id: Number) => {
  const res = await (await axios.get(`/api/products/${product_id}`)).data;
  // console.log(res)
  return res;
};
</script>

<style scoped>
a {
  color: #42b983;
}

label {
  margin: 0 0.5em;
  font-weight: bold;
}

code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}
</style>
