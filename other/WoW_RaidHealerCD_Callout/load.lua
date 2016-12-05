function(e, ...)
    event = select(2, ...)
    source = select(5, ...)
    dest = select(9, ...)
    
    source_class = select(2, UnitClass(source))
    source_color = RAID_CLASS_COLORS[source_class].colorStr
    
    dest_class = select(2, UnitClass(dest))
    dest_color = RAID_CLASS_COLORS[dest_class].colorStr
    
    spell = select(1, select(4, select(10, ...)))
    if event == "SPELL_CAST_SUCCESS" then
        if spell == "Innervate" then
            local s = source .. " innervated " .. dest
            local sf = "\124c"..source_color..""..source .. "\124r innervated \124c" .. dest_color .. dest .. "\124r"
            if aura_env.messager_mode == true then
                SendChatMessage(s, aura_env.raid_cd_msgmode[spell])
            end
            aura_env.display = sf
            return true
        end
        
        for _,v in pairs(aura_env.raid_instahealer_cds) do
            if v == spell then
                local s = source .. " used " .. spell
                local sf = "\124c"..source_color..""..source .. "\124r used \124c" .. source_color .. spell .. "\124r"
                aura_env.display = sf
                if aura_env.messager_mode == true then
                    SendChatMessage(s, aura_env.raid_cd_msgmode[spell])
                end
                
                return true
            end
        end
    end
    
    if event == "SPELL_AURA_APPLIED" and dest == source then
        for _,v in pairs(aura_env.raid_channelhealer_cds) do
            if v == spell and spell ~= aura_env.last_used_cd then
                aura_env.last_used_cd = spell
                local s = source .. " is using " .. spell
                local sf = "\124c"..source_color..""..source .. "\124r is using \124c" .. source_color .. spell .. "\124r"
                aura_env.display = sf
                if aura_env.messager_mode == true then
                    SendChatMessage(s, aura_env.raid_cd_msgmode[spell])
                end
                return true
            end 
        end
        
    end
    return false
end
