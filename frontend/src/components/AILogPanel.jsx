export default function AILogPanel() {

  const logs = [
    "Survivor detected near collapsed building",
    "EDGE AI analyzing thermal image",
    "Drone D-02 redirected",
    "Rescue probability: 91%",
  ];

  return (
    <div className="bg-gray-900 p-4 rounded-xl h-[500px] overflow-y-auto">

      <h2 className="text-green-400 text-xl font-bold">
        AI LIVE FEED
      </h2>

      <div className="mt-4 space-y-3">
        {logs.map((log, index) => (
          <div key={index} className="bg-black p-2 rounded">
            [AI] {log}
          </div>
        ))}
      </div>

    </div>
  );
}