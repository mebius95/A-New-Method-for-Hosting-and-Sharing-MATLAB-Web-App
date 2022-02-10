function out=daizu(ap,as,fpl,fph,fsl,fsh)
    fs=1000;
    omegapl=2*pi*fpl/fs/pi;
    omegaph=2*pi*fph/fs/pi;
    omegasl=2*pi*fsl/fs/pi;
    omegash=2*pi*fsh/fs/pi;
    [N,wn]=buttord([omegapl omegaph],[omegasl omegash],ap,as);
    [bz,az]=butter(N,wn,"stop");
    [h,f]=freqz(bz,az,1024,"whole",fs);
    disp("分子系数b");
    fprintf("%.4e   ",bz);
    fprintf('\n');
    disp('分母系数a');fprintf('%.4e    ',az);fprintf('\n');
    out=N;
    ampli=20*log10(abs(h));
    figure
    plot(f(1:512),ampli(1:512),"k")
    xlabel("频率/Hz");ylabel("幅度/dB");grid;
    saveas(1,"D:\image\带阻幅度响应.jpg");
    figure
    [theta,fx]=phasez(bz,az,1024,"whole",fs);
    plot(fx(1:512),theta(1:512)*360/(2*pi),"k");
    xlabel("频率/Hz");ylabel("相位/°");grid;
    saveas(2,"D:\image\带阻相位响应.jpg");
end