function out = HighpassHanning(wp,ws)
    Bt=wp-ws;
    N0=ceil(6.2*pi/Bt);
    N=N0+mod(N0+1,2);
    out=N;
    wc=(wp+ws)/2/pi;
    hn=fir1(N-1,wc,"high",hanning(N));
    figure;
    stem(hn)
    xlabel('n')
    ylabel('h(n)')
    %saveas(1,['D:\nginx-1.20.2\html\tinydemo','单位冲激响应.jpg'])
    %grid;
    figure;
    [H,w]=freqz(hn,1);
    plot(w/pi,20*log10(abs(H)))
    xlabel("\omega/\pi")
    ylabel("幅度/dB")
    %saveas(2,['D:\nginx-1.20.2\html\tinydemo','幅度响应.jpg'])
    %grid;
    figure;
    [theta,w1]=phasez(hn,1);
    plot(w1/pi,theta*180/pi)
    xlabel("\omega//\pi")
    ylabel("相位/°")
    %saveas(3,['D:\nginx-1.20.2\html\tinydemo','相位响应.jpg'])
    %grid;
    filepath=pwd;           %保存当前工作目录
    cd('D:\nginx-1.20.2\html\tinydemo')          %把当前工作目录切换到指定文件夹
    saveas(1,'单位冲激响应.jpg')
    grid;
    saveas(2,'幅度响应.jpg')
    grid;
    saveas(3,'相位响应.jpg')
    grid;
    cd(filepath)            %切回原工作目录
end