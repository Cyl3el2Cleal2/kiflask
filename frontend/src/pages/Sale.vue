<template>
  <div class="h-screen w-full max-w-full flex">
    <div class="flex flex-wrap flex-grow justify-center items-baseline overflow-y-auto">
      <Product
        v-for="n in 20"
        :key="n"
        @basketUpdate="basketUpdate"
        stock="5"
        class="w-4/5 md:w-80 mx-1 md:mx-3 my-6"
      />
    </div>

    <div class="bg-blue-400 w-1/3 md:w-1/4 h-screen flex flex-col">
      <div class="p-0 md:p-2">
        <div class="bg-white text-2xl  md:rounded-xl">Vending Machine</div>
        <h3 class="mt-6">Orders</h3>
        <div class="bg-blue-600 h-56 md:rounded-xl overflow-y-auto">
          <div v-for="detail in state.orderDetail" :key="detail.product_id">
            {{ detail.name }} : {{ detail.quantity }}
          </div>
        </div>
        <h2>Total: {{netPrice}}</h2>
        <button class="bg-green-500 w-full border-2 rounded-md border-gray-700" @click="isPayment=true">Pay</button>
        <input v-if="isPayment" type="number" class="w-full rounded-md text-base mt-2 px-2" placeholder="Enter money">
        <button v-if="isPayment" class="bg-green-500 w-full border-2 rounded-md border-gray-700 mt-2" :disabled="true" @click="isPayment=true">OK</button>
        <button class="bg-red-500 w-full text-white border-2 rounded-md border-red-50 mt-2" @click="cancleOrder">Cancle</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Product from "../components/Product.vue";

export default defineComponent({
  name: "Sale",
  components: {
    Product,
  },
  setup: () => {
    const netPrice = ref(0);
    const state = ref({
      orderDetail: [],
    });

    const isPayment = ref(false);

    const basketUpdate = async (id, count, name) => {
      // console.log(id, count);
      const product = state.value.orderDetail.find(
        (product) => (product.product_id = id)
      );
      const productIndex = state.value.orderDetail.indexOf(product);

      // Not in basket so add it
      if (productIndex === -1) {
        state.value.orderDetail.push({
          product_id: id,
          quantity: count,
          name: name,
        });
        return;
      }

      // Quantity = 0 delete from the basket
      if (count === 0 && productIndex >= 0) {
        const removedTheProductArr = state.value.orderDetail.filter(
          (product) => product.product_id !== id
        );
        state.value.orderDetail = removedTheProductArr;
        return;
      }

      // Change the number in basket
      state.value.orderDetail[productIndex]["quantity"] = count;
    };

    const cancleOrder = async () => {
      window.location.reload()
    }
    return {
      netPrice,
      state,
      basketUpdate,
      isPayment,
      cancleOrder
    };
  },
});
</script>

<style>
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
</style>