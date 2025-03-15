using XLSX

mutable struct Record
    gname :: String
    n :: Int
    m :: Int
    m_lg :: Int
    m_en :: Int
    score_lg :: Float64
    score_en :: Float64
end

function emptyRec()
    return Record("",0,0,0,0,0.0,0.0)
end

function runMain()
    lst = []
    cnt = nothing
    open("result.txt", "r") do f1
        i = -1
        for line in eachline(f1)
            buf = split(line)
            if size(buf, 1)<3; continue; end
            if size(buf, 1)==3
                i = 1
                cnt = emptyRec()
                cnt.gname = String(buf[1])
                cnt.n = parse(Int, buf[2])
                cnt.m = parse(Int, buf[3])
                continue
            end
            i += 1
            if i==2; cnt.m_lg = parse(Int, buf[5]); continue; end
            if i==3; cnt.score_lg = parse(Float64, buf[5]); continue; end
            if i==4; cnt.m_en = parse(Int, buf[5]); continue; end
            if i==5 
                cnt.score_en = parse(Float64, buf[5]) 
                push!(lst, deepcopy(cnt))
                continue 
            end
        end
    end

    sort!(lst, by=x->x.n)

    XLSX.openxlsx("result.xlsx", mode="rw") do xf
        sheet = xf[1]
        for i = 1 : size(lst, 1)
            x = lst[i] 
            sheet[i+1, :] = [x.gname, x.n, x.m, x.m_lg, x.m_en, x.score_lg, x.score_en]
        end
    end
end

runMain()