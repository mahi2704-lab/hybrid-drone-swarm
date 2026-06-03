export default function DisasterPanel() {
  return (
    <div className="bg-gray-900 p-4 rounded-xl mt-4">
      <h2 className="text-red-400 text-xl font-bold">
        DISASTER ALERT
      </h2>

      <div className="mt-3 space-y-2">
        <p>Type: Flood</p>
        <p>Severity: HIGH</p>
        <p>Location: Chennai Coastal Zone</p>
        <p>Affected Radius: 4.2 km</p>
      </div>
    </div>
  );
}