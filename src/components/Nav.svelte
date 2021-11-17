<script>
  export let segment;
</script>

<nav>
  <ul>
    {#if segment}
    <li>
      <a href=".">home</a>
    </li>
    {:else}
    <li class="selected">
      <span>home</span>
    </li>
    {/if}
    {#if segment != "projetos"}
    <li>
      <a href="projetos">/projetos</a>
    </li>
    {:else}
    <li class="selected">
      <span>/projetos</span>
    </li>
    {/if}
    {#if segment != "uses"}
    <li>
      <a href="uses">/uses</a>
    </li>
    {:else}
    <li class="selected">
      <span>/uses</span>
    </li>
    {/if}
    {#if segment != "academic"}
    <li>
      <a href="academic">/academic</a>
    </li>
    {:else}
    <li class="selected">
      <span>/academic</span>
    </li>
    {/if}
  </ul>
</nav>

<style>
nav {
  margin-bottom: 1rem;
}
ul {
  display: flex;
  flex-direction: row;
  gap: .25rem;
}
ul li {
  position: relative;
  padding: .25rem .5rem;
}
ul li:not(.selected):hover {
  background-color: #f9f9f9;
  background-color: var(--softest-highlight, #f9f9f9);
}
li.selected {
  background-color: #efefef;
  background-color: var(--soft-highlight, #efefef);
  border-radius: 4px;
}
a[href] {
  position: relative;
}
a[href]:hover, a[href]:active, a[href]:focus {
  text-decoration: none;
}
span {
  color: #444;
  color: var(--black, #444);
}
li.selected::after {
  content: "";
  display: block;
  position: absolute;
  left: 50%;
  width: .75rem;
  height: .2rem;
  margin-top: .2rem;
  border-radius: 1rem;
  transform: translate(-50%);
}
li.selected::after {
  background-color: #0b7dda;
  background-color: var(--accent, #0b7dda);
}
</style>