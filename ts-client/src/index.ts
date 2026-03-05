export type HealthResponse = { status: "ok" | string };

export async function getHealth(baseUrl: string): Promise<HealthResponse> {
  const res = await fetch(`${baseUrl}/health`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return (await res.json()) as HealthResponse;
}
