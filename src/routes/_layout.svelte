<script>
  import BigHeader from "../components/BigHeader.svelte";
  import Header from "../components/Header.svelte";
  export let segment;

  import { stores } from "@sapper/app";
  const { page } = stores();
</script>

{#if $page.path == "/"}
  <BigHeader {segment}/>
  <slot/>
{:else}
  <Header {segment}/>
  <slot/>
{/if}