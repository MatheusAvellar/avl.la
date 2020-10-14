<script>
  import Nav from "./Nav.svelte";
  export let segment = "?";
</script>

<header>
  <h1><span>avellar</span>/{segment}</h1>
  <Nav {segment}/>
</header>

<style>
h1 {
  font-size: 3.5rem;
}
span {
  color: #99999e;
}
</style>