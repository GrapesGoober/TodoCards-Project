<script>
    import CardTemplate from "./CardTemplate.svelte";
    import DeckTemplate from "./DeckTemplate.svelte";
    import PingTemplate from "./PingTemplate.svelte";
    import UserTemplate from "./UserTemplate.svelte";
    import EditCardTemplate from "./EditCardTemplate.svelte";
</script>

<h1>This is a demo for the APIs</h1>

<h2>Try pinging the server</h2>
<PingTemplate></PingTemplate>

<h2>Log in first</h2>
<UserTemplate></UserTemplate>

<h2>Some decks-list test</h2>
<DeckTemplate></DeckTemplate>

<h2>Some cards-list test</h2>
<CardTemplate></CardTemplate>

<h2>Some editing card</h2>
<EditCardTemplate></EditCardTemplate>