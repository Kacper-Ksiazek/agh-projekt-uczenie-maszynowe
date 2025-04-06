<script lang="ts">
import { QueryClient, QueryClientProvider } from "@tanstack/svelte-query";
import { Toaster } from "$lib/components/ui/sonner";
import "../app.css";
let { children } = $props();

const queryClient = new QueryClient();
</script>

<svelte:head>
  <title>AI Generator Diet | IiAD</title>
</svelte:head>

<Toaster />

<QueryClientProvider client={queryClient}>
  <main class="flex h-[100dvh] flex-col">
    {@render children()}
  </main>
</QueryClientProvider>
