import { useState } from "react";

const LiveView = () => {
  const [videoSource, setVideoSource] = useState("/path-to-your-video.mp4");

  const handleVideoChange = (event) => {
    const channel = event.target.value;
    setVideoSource(`/videos/channel${channel}.mp4`);
  };

  return (
    <div className="flex flex-col justify-start items-center h-screen">
      <select 
        onChange={handleVideoChange} 
        className="mb-5 p-2 border rounded"
      >
        {Array.from({ length: 10 }, (_, i) => i + 1).map((channel) => (
          <option key={channel} value={channel}>
            Channel {channel}
          </option>
        ))}
      </select>

      <video 
        controls 
        autoPlay 
        className="w-full max-w-3xl mt-10"
      >
        <source src={videoSource} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default LiveView;
