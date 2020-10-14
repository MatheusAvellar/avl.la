<script>
  export let status;
  export let error;

  import Footer from "../components/Footer.svelte";
  import T2 from "../components/T2.svelte";
</script>

<svelte:head>
  <title>{status} | Matheus Avellar</title>
</svelte:head>

<main>
  {#if status == 404}
    <T2>404</T2>

    <p>Não sei onde você queria ir, mas não era pra cá!</p>
  {:else}
    <h2>{status}</h2>
    <p>{error.message}</p>
  {/if}
</main>
<Footer/>