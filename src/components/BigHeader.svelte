<script>
  import Nav from "./Nav.svelte";
  import Hr from "./Hr.svelte";
  export let segment = "";
</script>

<header>
  <h1> Matheus Avellar </h1>
  <Nav {segment}/>
  <Hr/>
</header>

<style>
h1 {
  font-size: 3.5rem;
  line-height: normal;
  margin-top: -.175em;
}
@media screen and (max-width: 800px) {
  h1 {
    font-size: 2.5rem;
  }
}
</style>