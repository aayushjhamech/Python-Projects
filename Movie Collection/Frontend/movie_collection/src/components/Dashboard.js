import React, {useEffect, useState } from "react";
import Navbar from "./Navbar";
import "./Dashboard.css";
import React from 'react';
import axios from 'axios';

const Dashboard = () =>{
    const [allVideos, setAllVideos]= useState(null);
    const [source, setSource] = useState("");
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");
    const [hashtags, setHashtags] = useState("");


    const videoData= (object) => {
            setSource(object.url);
            setTitle(object.title);
            setDesc(object.description);
            setHashtags(object.hashtags);
    };
};

export default Dashboard;
